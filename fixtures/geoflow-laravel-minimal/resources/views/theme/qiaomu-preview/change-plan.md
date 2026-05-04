# Theme Edit Session

- Base theme: `default`
- Preview theme: `qiaomu-preview`
- Framework: `laravel`
- Requested changes: Fixture-only landing reroute drill; keep preview separate from activation.
- Finalize options: `publish_as_new_theme` | `replace_base_theme` | `activate_after_confirmation`

## Preview Checklist

- [x] keep edits scoped to `qiaomu-preview`
- [x] point preview Blade includes at `theme.qiaomu-preview.partials.*`
- [x] apply a small editorial home/card styling slice
- [x] update preview tokens and mapping metadata
- [ ] review home/category/article/archive preview routes in a real app shell
- [ ] confirm GEOFlow data placeholders still render correctly
- [ ] keep production activation out of scope
