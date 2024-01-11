/**
 * JavaScript script that fetches and prints how to say “Hello” depending on the language.
 */

$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const input = $('input#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/',
      {
        lang: input
      },
      function (data, textStatus) {
        $('INPUT#btn_translate').css('cursor', 'pointer').click(function () {
          $('div#hello').text(data.hello);
        });
      });
  });
});
