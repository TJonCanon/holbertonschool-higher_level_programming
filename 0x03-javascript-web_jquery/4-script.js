const header = $('header');
$('DIV#toggle_header').on('click', function (event) {
  header.toggleClass('red green');
});