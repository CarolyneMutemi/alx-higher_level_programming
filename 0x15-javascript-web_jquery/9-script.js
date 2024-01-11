/**
 * JavaScript script that fetches from given URL and displays
 * the value of hello from that fetch in the HTML tag DIV#hello.
 */
$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr',
    {
      lang: $('html').attr('lang')
    },
    function (data, textStatus) {
      $('div#hello').text(data.hello);
    });
});
