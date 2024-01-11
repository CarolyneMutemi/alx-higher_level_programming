/**
 * JavaScript script that fetches the character name from given URL.
 */

$.ajax({
  type: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  success: function (data) {
    $('DIV#character').text(data.name);
  }
});
