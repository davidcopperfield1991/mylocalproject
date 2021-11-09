$(document).ready(function () {

    function msToTime(s) {

        // Pad to 2 or 3 digits, default is 2
        function pad(n, z) {
            z = z || 2;
            return ('00' + n).slice(-z);
        }

        var ms = s % 1000;
        s = (s - ms) / 1000;
        var secs = s % 60;
        s = (s - secs) / 60;
        var mins = s % 60;
        var hrs = (s - mins) / 60;

        return pad(hrs) + ':' + pad(mins) + ':' + pad(secs)
    }

    // let formatted1 = 0;
    var starttime = 0 ;
    var stoptime = 0 ;

    $("#start").click(function (e) {

        var now = new Date($.now());
        var formatted1 = now.getHours() + ":" + now.getMinutes() + ":" + now.getSeconds();
        $("#startinput").val(formatted1);
        return starttime = now
    });



    $("#pause").click(function (e) {
        var now = new Date($.now());
        var formatted2 = now.getHours() + ":" + now.getMinutes() + ":" + now.getSeconds();
        $("#stopinput").val(formatted2);
        return stoptime = now

    });

    $("#reset").click(function (e) {
        var total =  stoptime - starttime ;
        var totall = msToTime(total)
        // var totall = total.getHours() + ":" + total.getMinutes() + ":" + total.getSeconds();
        // alert(totall);
        $("#totalinput").val(totall);
        // alert(starttime);
        // alert(stoptime);

    });


    $("#sawoj").mouseup(function(){

        var str = $("#sawoj").val();

        $.ajax({
            method: "GET",
            url: "stopwatch",
            data: { name: str },
            success: function (data){
                if (data.msg == 'success'){
                    let job=[]
                    let onwan =JSON.parse(data.pul)
                    $("#sawojbolagh").empty()
                    for (let i = 0; i < onwan.length; i++) {

                        $("#sawojbolagh").append(`<option>
                                       ${onwan[i].fields.title}
                                  </option>`);

                    }
                    // $("#sawojbolagh").val('');
                    // $("#description").val(job);
                    // $("#description").append(`<option>
                    //                    ${job}
                    //               </option>`);
                    // alert('salam dadash');

                }
            }
        }).done(function() {
            $( this ).addClass( "done" );

        });
    });

});