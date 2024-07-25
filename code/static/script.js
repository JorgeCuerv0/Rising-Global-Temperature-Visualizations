$(document).ready(function(){
    // Enable smooth scrolling
    $('.nav-link').click(function(e){
        e.preventDefault();
        var target = $(this).attr('href');
        $('html, body').animate({
            scrollTop: $(target).offset().top
        }, 500);

        // Collapse the menu when a link is clicked
        $('.navbar-collapse').collapse('hide');
    });

    // Enable scrollspy to update the navbar links based on scroll position
    $('body').scrollspy({ target: '#navbar-example' });
});
