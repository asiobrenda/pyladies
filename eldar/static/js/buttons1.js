var add_path = document.getElementById('add_tab').getAttribute('data_path');
function addTab(evt){
   //alert(11111)
   var name = prompt("Enter tab name");
   //alert(name)
   if (!name){alert('Please enter city name'); return};
   dic = {'cityName':name, 'description':'Add any city name', 'color': 'yellow'};
   //alert(JSON.stringify(dic))
   //alert(22)
   //alert(add_path)
     $.post(add_path,
        {
            'dic': JSON.stringify(dic),
        },
        function(data) {
            //alert(JSON.stringify(data))
            var tab_id = data['tab_id'];
            var name = data['name'];
            var color = data['color'];
            var description = data['description'];
            create_tab(tab_id, name, description, color);
        });

}

function create_tab(tab_id, name, description, color){
      //alert(33333)

    var button_ = document.createElement("button");
    button_.setAttribute("class", "tablinks");
    button_.setAttribute("onclick", "openCity(event, '" + color + "')");
    button_.setAttribute("tab_id", tab_id);
    button_.setAttribute("id", tab_id);
    //alert(button_.innerHTML)
    button_.innerHTML = name;
    var tab = document.getElementById('add_button');
    tab.appendChild(button_)


    var tabContent = document.createElement("div");
    tabContent.setAttribute("id", 'new_tab_' + tab_id);
    tabContent.setAttribute("class", "tabcontent");
    //tabContent.style.display = "none";
    tabContent.innerHTML = "<h3>" + name + "</h3><p>" + description + "</p>";

    // Append to the body
    var body_ = document.getElementById("content_id");
    body_.appendChild(tabContent);


}

var get_path = document.getElementById('add_button').getAttribute('url_path');
function get_data(event){
alert(55555)
   alert(get_path)
        $.post(get_path,
        {

        },
        function(data) {
            alert(JSON.stringify(data))
              for (var d in data){
              var tab_id = d;
               var name = data[d]['name'];
              var description = data[d]['description'];
             var color = data[d]['color']
           //alert(tab_name)
            create_tab(tab_id, name, description, color)
    }
        });

}


var div_ = document.createElement("div");
function openCity(evt, color) {
   event = evt.target;
   //alert(event)
   tab_id = event.getAttribute('tab_id');
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
  document.getElementById('new_tab_' + tab_id).style.display = "block";
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