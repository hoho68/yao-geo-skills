@include('theme.qiaomu-preview.partials.header')

<main class="theme-shell">
  <section class="page-heading">
    <p class="eyebrow">Fixture Category</p>
    <h1>{{ $category['name'] ?? 'Category name' }}</h1>
    <p>{{ $category['description'] ?? 'Category description placeholder.' }}</p>
  </section>

  <section class="article-list">
    @foreach (($articles ?? []) as $article)
      <article class="article-card">
        <h2>{{ $article['title'] ?? 'Article title' }}</h2>
        <p>{{ $article['excerpt'] ?? 'Article excerpt placeholder.' }}</p>
      </article>
    @endforeach
  </section>
</main>

@include('theme.qiaomu-preview.partials.footer')
