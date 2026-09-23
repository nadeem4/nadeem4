import unittest

import profile_projects as pp


def repo(name, topics=(), **kw):
    base = {
        "name": name,
        "html_url": f"https://github.com/nadeem4/{name}",
        "description": f"{name} description.",
        "homepage": "",
        "topics": list(topics),
        "fork": False,
        "archived": False,
        "stargazers_count": 0,
    }
    base.update(kw)
    return base


class WrapTest(unittest.TestCase):
    def test_breaks_on_word_boundaries(self):
        self.assertEqual(pp.wrap("aaa bbb ccc", 7, 3), ["aaa bbb", "ccc"])

    def test_truncates_with_ellipsis_when_out_of_lines(self):
        self.assertEqual(pp.wrap("aaa bbb ccc ddd", 7, 1), ["aaa…"])

    def test_empty_text_gives_no_lines(self):
        self.assertEqual(pp.wrap("", 10, 3), [])


class SelectTest(unittest.TestCase):
    def test_live_demo_topic_makes_a_poster_and_featured_makes_a_row(self):
        live, building = pp.select(
            [
                repo("demo", ["live-demo"], homepage="https://demo.example"),
                repo("lib", ["featured", "status-alpha"]),
                repo("other"),
            ],
            {},
        )
        self.assertEqual([p["name"] for p in live], ["demo"])
        self.assertEqual(live[0]["demo"], "https://demo.example")
        self.assertEqual([p["name"] for p in building], ["lib"])
        self.assertEqual(building[0]["status"], "alpha")

    def test_live_demo_without_a_url_is_skipped(self):
        live, _ = pp.select([repo("demo", ["live-demo"])], {})
        self.assertEqual(live, [])

    def test_forks_and_archived_repos_are_ignored(self):
        live, building = pp.select(
            [repo("f", ["featured"], fork=True), repo("a", ["featured"], archived=True)], {}
        )
        self.assertEqual((live, building), ([], []))

    def test_a_repo_with_both_topics_only_appears_as_a_poster(self):
        live, building = pp.select(
            [repo("x", ["live-demo", "featured"], homepage="https://x.example")], {}
        )
        self.assertEqual(len(live), 1)
        self.assertEqual(building, [])

    def test_overrides_replace_repo_metadata(self):
        live, _ = pp.select(
            [repo("x", ["live-demo"], homepage="https://docs.example")],
            {"x": {"demo": "https://demo.example", "tagline": "Short.", "cta": "Go"}},
        )
        self.assertEqual(live[0]["demo"], "https://demo.example")
        self.assertEqual(live[0]["tagline"], "Short.")
        self.assertEqual(live[0]["cta"], "Go")

    def test_title_defaults_to_repo_name_and_can_be_overridden(self):
        live, _ = pp.select(
            [repo("x", ["live-demo"], homepage="https://x.example"),
             repo("y", ["live-demo"], homepage="https://y.example")],
            {"y": {"title": "Why"}},
        )
        self.assertEqual([p["title"] for p in live], ["x", "Why"])

    def test_ordered_by_stars_then_name(self):
        _, building = pp.select(
            [
                repo("b", ["featured"]),
                repo("a", ["featured"]),
                repo("c", ["featured"], stargazers_count=5),
            ],
            {},
        )
        self.assertEqual([p["name"] for p in building], ["c", "a", "b"])

    def test_row_without_status_topic_is_active(self):
        _, building = pp.select([repo("x", ["featured"])], {})
        self.assertEqual(building[0]["status"], "active")


class HostTest(unittest.TestCase):
    def test_hugging_face_urls_are_named(self):
        self.assertEqual(pp.host_label("https://nadeem4nk-x.hf.space/"), "Hugging Face")
        self.assertEqual(pp.host_label("https://huggingface.co/spaces/a/b"), "Hugging Face")

    def test_other_urls_show_their_host(self):
        self.assertEqual(pp.host_label("https://arena.codewithnk.com/x"), "arena.codewithnk.com")


class RenderTest(unittest.TestCase):
    def setUp(self):
        self.project = {
            "name": "a&b",
            "title": "T&itle",
            "tagline": "Uses <tags> & ampersands.",
            "demo": "https://x.hf.space/",
            "cta": "Try it",
            "url": "https://github.com/nadeem4/a",
            "status": "alpha",
        }

    def test_poster_escapes_text_and_uses_palette(self):
        svg = pp.render_poster(self.project, pp.PALETTES["dark"], "")
        self.assertIn("T&amp;itle", svg)
        self.assertIn("&lt;tags&gt;", svg)
        self.assertIn(pp.PALETTES["dark"]["amber"], svg)
        self.assertIn("Try it →", svg)

    def test_poster_fills_viz_tokens_from_palette(self):
        svg = pp.render_poster(self.project, pp.PALETTES["light"], '<circle fill="{{amber}}"/>')
        self.assertIn(f'<circle fill="{pp.PALETTES["light"]["amber"]}"/>', svg)
        self.assertNotIn("{{", svg)

    def test_row_shows_status_label(self):
        svg = pp.render_row(self.project, pp.PALETTES["light"])
        self.assertIn(">ALPHA<", svg)
        self.assertIn("a&amp;b", svg)


    def test_row_descriptions_line_up_whatever_the_name_length(self):
        import re
        xs = set()
        for name in ["ab", "a_much_longer_repo_name_than_most"]:
            svg = pp.render_row({**self.project, "name": name}, pp.PALETTES["light"])
            xs.add(re.findall(r'<text x="(\d+)"', svg)[1])
        self.assertEqual(len(xs), 1)

    def test_long_row_names_are_shortened(self):
        svg = pp.render_row({**self.project, "name": "x" * 40}, pp.PALETTES["light"])
        self.assertNotIn(">" + "x" * 40 + "<", svg)
        self.assertIn("…", svg)


class BlockTest(unittest.TestCase):
    def test_block_links_images_to_demo_and_repo(self):
        block = pp.render_block(
            [{"name": "d", "demo": "https://d.example", "tagline": "T"}],
            [{"name": "r", "url": "https://github.com/nadeem4/r", "tagline": "R"}],
        )
        self.assertIn('<a href="https://d.example">', block)
        self.assertIn("assets/projects/d-dark.svg", block)
        self.assertIn('<a href="https://github.com/nadeem4/r">', block)
        self.assertIn("assets/projects/row-r-light.svg", block)

    def test_empty_sections_are_left_out(self):
        block = pp.render_block([], [{"name": "r", "url": "u", "tagline": "R"}])
        self.assertNotIn("Try it live", block)
        self.assertIn("In progress", block)

    def test_replace_block_only_touches_the_marked_region(self):
        readme = "top\n<!-- PROJECTS:START -->\nold\n<!-- PROJECTS:END -->\nbottom"
        out = pp.replace_block(readme, "new")
        self.assertEqual(out, "top\n<!-- PROJECTS:START -->\nnew\n<!-- PROJECTS:END -->\nbottom")

    def test_replace_block_fails_loudly_without_markers(self):
        with self.assertRaises(ValueError):
            pp.replace_block("no markers here", "new")


if __name__ == "__main__":
    unittest.main()
