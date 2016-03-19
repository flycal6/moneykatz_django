/**
 * Created by brianthomas on 3/1/16.
 */

var aboutbtn = $('#about-btn');

$(document).ready(function() {
    aboutbtn.click(function(event) {
        $(this).addClass('btn btn-primary');
    });
});

$(document).ready(function() {
    $('.addcat').click(function(event) {
        $('i.addcat').toggleClass('fa-folder-o fa-spinner fa-pulse');
    });
});

$(document).ready(function() {
    $('.addfile').click(function(event) {
        $('i.addfile').toggleClass('fa-cloud-upload fa-spinner fa-pulse');
    });
});

$('.content-container').css('min-height',$(window).height());