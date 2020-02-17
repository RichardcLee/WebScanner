// need process string
$('.tips ol li').click(function (){
    text = $(this).children('span').text();
    //$('form.search input').val(text);
    $('.warn').attr('placeholder', 'Example:'+text);

    $('form.search input').focus();
    $('.warn').attr('alt', 'Example:'+text);
})