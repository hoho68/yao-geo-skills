<?php

/*
|--------------------------------------------------------------------------
| Minimal fixture routes
|--------------------------------------------------------------------------
|
| These route declarations are placeholders for theme discovery tests only.
| The fixture is not a runnable Laravel application.
|
*/

Route::view('/', 'site.home')->name('home');
Route::view('/category/{slug}', 'site.category')->name('category.show');
Route::view('/article/{slug}', 'site.article')->name('article.show');
Route::view('/archive', 'site.archive')->name('archive');
