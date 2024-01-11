/**
 * JavaScript script that toggles the class of the <header>
 * element when the user clicks on the tag DIV#toggle_header.
 */

$('div#toggle_header').css('cursor', 'pointer').addClass('red').click(function () {
  $(this).toggleClass('red green');
});
