/**
 * Created by brianthomas on 3/1/16.
 */

var aboutbtn = $('#about-btn');
var msg = '#msg';

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