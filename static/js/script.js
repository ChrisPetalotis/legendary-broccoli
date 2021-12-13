$(document).ready(function () {

	// Assign event listeners
	$(window).scroll(() => showArrowToTop());
	$('#arrow-to-top').click((event) => scrollToTop(event));
	$('.nav-item>a').click(function(event) {
		const targetSection = $(this).attr("href");
		if (!targetSection.includes('html')) {
			event.preventDefault();
			const marginTop = parseInt($(targetSection).css('margin-top'), 10)
			$('html, body').animate({ scrollTop: $(targetSection).offset().top - marginTop}, 750);
		}
	})
});


function showArrowToTop() {
	// When the user scrolls down 450px from the top of the document, show the scroll-to-top-button
	if ($(document).scrollTop() > 450) {
		$("#arrow-to-top").addClass('active');
	}
	else {
		$("#arrow-to-top").removeClass('active');
	}
	
	$(".arrowDown").css("opacity", 1 - $(window).scrollTop() / 5000);
}
// When the user clicks on the arrow button, scroll to the top of the document
function scrollToTop(event) {
	event.preventDefault();
	$('html, body').animate({
  		scrollTop: 0
	}, 900);
}