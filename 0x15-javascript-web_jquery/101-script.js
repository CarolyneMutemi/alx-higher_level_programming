/**
 * JavaScript script that adds, removes and clears LI elements from a list when the user clicks.
 */

$(document).ready(function () {
  $('div#add_item').css('cursor', 'pointer').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });
  $('div#remove_item').css('cursor', 'pointer').click(function () {
    $('ul.my_list').children().last().remove();
  });
  $('div#clear_list').css('cursor', 'pointer').click(function () {
    $('ul.my_list').empty();
  });
});
