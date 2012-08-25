/* Author: Awesome Antonn Esquivel */

$(document).ready(function(){

	if (exists('#fileselectbutton')) {
		fileinputbootstrap();
	}

	// Posts
	$('li.post').each(function (index) {
		scrollfixcontainer('.post-info', $(this).attr('class').split(' ')[1]);
	});

});

/* If element exists */
function exists (element) {
	return $(element).is('*');
}

/* File input bootstrap look hack */
function fileinputbootstrap () {
	$('#fileselectbutton').click(function(e){
		$('#file').trigger('click');
	});

	$('#file').change(function(e){
		var val = $(this).val();

		var file = val.split(/[\\/]/);

		$('#filename').val(file[file.length-1]);
	});
}

/* Scroll down to Fixed */
function scrollfix (element) {
	var top = $(element).offset().top - parseFloat($(element).css('marginTop').replace(/auto/, 0));
	top -= $('header#top').height(); // Relative to header height

	$(window).scroll(function (event) {
		var y = $(this).scrollTop();

		if (y >= top && !$(element).hasClass('fixed')) {
			$(element).addClass('fixed');
		} else if (y < top && $(element).hasClass('fixed')) {
			$(element).removeClass('fixed');
		}
	});
}

function scrollfixcontainer (element, parent) {
	//alert(element + ' ' + parent);
}