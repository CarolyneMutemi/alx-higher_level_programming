/**
 * JavaScript script that fetches and prints how to say “Hello” depending on the language.
 */

$(document).ready(function () {
  const input = $('input#language_code').val();
  $.get('https://hellosalut.stefanbohacek.dev/?lang=en',
    {
      lang: input
    },
    function (data, textStatus) {
      console.log($('input#language_code').val());
      console.log(data);
      $('INPUT#btn_translate').css('cursor', 'pointer').click(function () {
        $('div#hello').text(data.hello);
      });
    });
});
