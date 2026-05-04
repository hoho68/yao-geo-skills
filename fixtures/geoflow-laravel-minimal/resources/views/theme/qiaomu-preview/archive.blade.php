@include('theme.qiaomu-preview.partials.header')

<main class="theme-shell">
  <section class="page-heading">
    <p class="eyebrow">Fixture Archive</p>
    <h1>Archive</h1>
  </section>

  <section class="archive-list">
    @foreach (($archive ?? []) as $item)
      <article class="archive-row">
        <span>{{ $item['date'] ?? '2026-05' }}</span>
        <a href="{{ $item['url'] ?? '#' }}">{{ $item['title'] ?? 'Archive item' }}</a>
      </article>
    @endforeach
  </section>
</main>

@include('theme.qiaomu-preview.partials.footer')
