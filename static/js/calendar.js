var time_json ={
    "time":[
        {"hour":"08:00"},
        {"hour":"08:30"},
        {"hour":"09:00"},
        {"hour":"09:30"},
        {"hour":"10:00"},
        {"hour":"10:30"},
        {"hour":"11:00"},
        {"hour":"11:30"},
        {"hour":"12:00"},
        {"hour":"12:30"},
        {"hour":"13:00"},
        {"hour":"13:30"},
        {"hour":"14:00"},
        {"hour":"14:30"},
        {"hour":"15:00"},
        {"hour":"15:30"},
        {"hour":"16:00"},
        {"hour":"16:30"},
        {"hour":"17:00"},
        {"hour":"17:30"},
        {"hour":"18:00"},
        {"hour":"18:30"},
        {"hour":"19:00"},
        {"hour":"19:30"}
    ]
};

$(document).ready(function() {
    calendar();
    time_calendar(time_json);
});

function calendar(){
    $.get('/api/calendar/',function(res){
        $.each(res,function(key,value){
            $.each(value, function(k,v){
                id1 = "#"+key+"_"+v.start_time.replace(':','');
                id2 = "#"+key+"_"+v.end_time.replace(':','');
                console.log('#'+key+"_"+v.end_time.replace(':',''))
                $(id1).css({background:'#ccc'}).html(v.name+"INicio");
                $(id2).html(v.name+"Fin");
            });

        })
    })
}

function time_calendar(time_json){
    var sides = "";
    sides +=   '<div class="fila contenedor">';
    sides +=   '<div class="columna boton"> << </div>';
    sides +=   '<div class="columna cabecera" id="monday">Monday</div>';
    sides +=   '<div class="columna cabecera" id="tuesday">Tuesday</div>';
    sides +=   '<div class="columna cabecera" id="wednesday">Wednesday</div>';
    sides +=   '<div class="columna cabecera" id="thursday">Thursday</div>';
    sides +=   '<div class="columna cabecera" id="friday">Friday</div>';
    sides +=   '<div class="columna boton" id=""> >> </div>';
    sides +=   '</div>';
    $.each(time_json,function(key,value){
        $.each(value, function(t,h){
            sides +=   '<div class="fila">';
            hour = h.hour.replace(':','')
            sides +=   '<div class="columna side">'+ h.hour +'</div>';
            sides +=   '<div class="columna" id="monday_'+ hour +'"></div>';
            sides +=   '<div class="columna" id="tuesday_'+ hour +'"></div>';
            sides +=   '<div class="columna" id="wednesday_'+ hour +'"></div>';
            sides +=   '<div class="columna" id="thursday_'+ hour +'"></div>';
            sides +=   '<div class="columna" id="friday_'+ hour +'"></div>';
            sides +=   '<div class="columna side" id="">'+ h.hour +'</div>';
            sides +=   '</div>';
        });
    })
    $('.sides').html(sides);
}
