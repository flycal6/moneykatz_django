/**
 * Created by brianthomas on 3/1/16.
 */

var aboutbtn = $('#about-btn');
var msg = '#msg';

$(document).ready(function() {
    aboutbtn.click(function(event) {
        $(this).addClass('btn btn-primary');
    });
    aboutbtn.click(function(event) {
        var msgstr = $(msg).html();
        msgstr += 'o';
        $(msg).html(msgstr);
    });
});
