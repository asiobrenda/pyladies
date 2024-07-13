//var url = event.currentTarget.dataset.url
var url = document.getElementById('url').getAttribute('data_path')
function addTab(event) {
    alert(1111)
    var tab_name = prompt('Enter City Name');
     if (!tab_name){alert('Please enter city name'); return};
        //alert(tab_name)
        dic = {'cityName': tab_name, 'description':'Add any city name', 'color': 'blue'};
        //alert(dic)
        alert(url)
        // post to database
        $.post(url,
        {
            'dic': JSON.stringify(dic),
        },
        function(data) {
            alert(JSON.stringify(data));
            var tab_id = data['tab_id'];
            var name = data['name'];
            var color = data['color'];
            var description = data['description'];
            create_tab(tab_id, name, description, color);
        });
    }


function create_tab(tab_id, name, description, color){
    //alert(8888)
    var button_ = document.createElement("button");
    button_.setAttribute("class", "tablinks");
    button_.setAttribute("onclick", "openCity(event, '" + color + "')");
    button_.setAttribute("tab_id", tab_id);
    button_.setAttribute("id", tab_id);
    //alert(button_.innerHTML)
    button_.innerHTML = name;

    var btn = document.getElementById("tab_container");
    btn.appendChild(button_)

     var txt = document.createElement("textarea");
         txt.setAttribute("id", 'txt_' + tab_id);
         txt.setAttribute("rows", '10');
         txt.setAttribute("cols", '30');
         txt.setAttribute("class", "tabcontent");
         txt.innerHTML += name + '\n' + '\n';
         txt.innerHTML += description;


         var tab_content = document.getElementById("content_id");
         tab_content.appendChild(txt)

}

var data_url = document.getElementById('tab_container').getAttribute('url_path')
function get_data(event){
    $.post(data_url,
    {},
    function(dic){
    //alert(JSON.stringify(dic))
    for (var d in dic){
        var tab_id = d;
        var name = dic[d]['city_name'];
        var description = dic[d]['description'];
        var color = dic[d]['color']
        //alert(tab_name)
        create_tab(tab_id, name, description, color)
    }
    });
}

var div_ = document.createElement("div");
function openCity(evt, color) {
  var event_ = evt.target;
  //alert(event_)
  //alert(222)
  var tab_id = event_.getAttribute('tab_id');
  //alert(tab_id)
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  //document.getElementById(tab_id).style.display = "block";
  document.getElementById('txt_' + tab_id).style.display = "block";
  evt.currentTarget.className += " active";


    div_.setAttribute("style", "height: 200px; width:200px; background-color:"+ color +"; cursor:pointer; position:absolute");
        div_.setAttribute("id", tab_id);
        var p = document.getElementById("demo");
        p.appendChild(div_)

        var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
                     //Use the 3 events
                     div_.onmousedown = function(e){
                          pos1 = e.clientX;
                          pos2 = e.clientY;

                          document.onmousemove = function(e){
                                 pos3 = pos1 - e.clientX;
                                 pos4 = pos2 - e.clientY;

                                 pos1 = e.clientX;
                                 pos2 = e.clientY;

                                 div_.style.left = (div_.offsetLeft - pos3) + 'px';
                                 div_.style.top = (div_.offsetTop - pos4) + 'px';


                          };
                     div_.onmouseup = function(e){
                             document.onmousemove = null;
                             document.onmousedown = null;
                     };
                     }

 }