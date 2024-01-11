/**
 * JavaScript script that adds a <li> element
 * to a list when the user clicks on the tag DIV#add_item
 */

$('DIV#add_item').css('cursor', 'pointer').click(function () {
  $('ul.my_list').append('<li>Item</li>');
});
