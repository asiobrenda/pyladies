function Admin(dic) {
}

Admin.prototype.create_elements = function(dic) {
    this.body_id = dic['body_'];
    this.tab_url = dic['url'];
    this.get_data_url = dic['get_data'];
    this.delete_url = dic['delete_data'];
    this.save_url = dic['save_url'];
    this.save_btn = dic['save_btn'];
    this.saved_btn = dic['saved_btn'];

    //alert(this.saved_btn)
    //(this.save_btn);

  // Call the necessary setup functions
    this.addTab();
    this.get_data();
};

Admin.prototype.addTab = function() {

    var self = this;
// ADD TAB
    var add_tab = document.createElement('button');
    add_tab.innerHTML = 'Add Tab';
    add_tab.onclick = function(event) {
        tab_name = prompt('Enter City Name').toLowerCase();
        if (!tab_name) {
            alert('Please enter City Name!');
            return;
        }
        dic = {'cityName': tab_name, 'description': 'Add any city name', 'color': 'lightgray'};
        $.post(self.tab_url, {
            'dic': JSON.stringify(dic),
        }, function(data) {
            var tab_id = data['tab_id'];
            var name = data['tab_name'];
            var color = data['color'];
            var description = data['description'];

            self.create_tab(tab_id, tab_name, description, color);
        }.bind(self));
    };
// DELETE TAB
    var delete_tab = document.createElement('button');
    delete_tab.innerHTML = 'Delete Tab';
    delete_tab.onclick = function(event) {
        var delTab = prompt("Enter name to delete: ");
        if (!delTab) {
            alert('Please enter city name');
            return;
        }
        $.post(self.delete_url, {
            'delTab': delTab,
        }, function(data) {
            var button_id = data['tab_id_'];
            clear_deleted(button_id);
        });
    }.bind(self);
// CLEAR DELETE
    function clear_deleted(button_id) {
        var delete_button = document.getElementById('del_'+ button_id);
        delete_button.outerHTML = '';
        var delete_txt = document.getElementById('txt_'+ button_id);
        delete_txt.outerHTML = '';
    }

    var div_ = document.createElement('div');
    div_.appendChild(add_tab);
    div_.appendChild(delete_tab);
    this.body_id.appendChild(div_);
};
;
var div_btn = document.createElement("div");
var div_txt = document.createElement("div")
var div_ = document.createElement("div_pop_up");
var div_move = document.createElement('div_move');
var div_elms = document.createElement('div_elms');
var btn_cp = document.createElement('button');
var div_cp_main = document.createElement('div');
var div_edit = document.createElement('div_edit');
var txt_area = document.createElement('textarea');
//var div_right = document.createElement('div_right')
var btn_left = document.createElement('button');

// CREATE TAB
Admin.prototype.create_tab = function(tab_id, tab_name, description, color) {
    var self = this;
    var button_ = document.createElement('button');
    button_.setAttribute("class", "tablinks");
    button_.setAttribute("tab_id", tab_id);
    button_.setAttribute("data-color", color);
    button_.setAttribute("id", "del_" + tab_id);
    button_.innerHTML = tab_name;
    button_.onclick = function(event) {
                event_ = event.target;
                var tab_id_ = event_.getAttribute('tab_id');
                //alert(tab_id_)

                var i, tabcontent_, tablinks;
                tabcontent_ = document.getElementsByClassName("tabcontent");
                for (i = 0; i < tabcontent_.length; i++) {
                    tabcontent_[i].style.display = "none";
                }
                tablinks = document.getElementsByClassName("tablinks");
                for (i = 0; i < tablinks.length; i++) {
                    tablinks[i].className = tablinks[i].className.replace(" active", "");
                }

                document.getElementById("txt_" + tab_id_).style.display = "block";
                document.getElementById('cp_' + tab_id_).style.display = "block";
                document.getElementById("left_div_" + tab_id_).style.display = "block";
                document.getElementById("right_div_" + tab_id_).style.display = "block";

                 function create_id(e){
                    obj.id = tab_id;
                    //alert(counter)

                    return function(){
                        return ++obj.id;
                    }
                  }
                   getID = create_id();

                    btn_cp.onclick = function(event){
                        //alert(1111)
                        var evt = event.target;
                        var copied_btn = evt.cloneNode(true);
                        //alert(copied_btn)
                         div_cp.onclick = function(event){
                              function getNum(){
                                 return getID();
                             }
                               var id = getNum();
                                  //alert(id)
                                copied_btn.setAttribute("id", "btn_id_" + id);
                                var offsetX = event.offsetX;
                                var offsetY = event.offsetY;

                               copied_btn.style.position = "absolute";
                               copied_btn.style.left = offsetX + "px";
                               copied_btn.style.top = offsetY + "px";

                               copied_btn.innerHTML = "button_" + id + '_'+offsetX + "_" +offsetY;

                               div_cp.appendChild(copied_btn);
                                div_cp.onclick = null;
                               var saved_btn = copied_btn.innerHTML;
                                   //alert(saved_btn)
                                 $.post(self.save_btn,{
                                   'tab_id': tab_id,
                                   'copied_btn_id': id,
                                   'tab_name': tab_name,
                                    'saved_btn': saved_btn,
                                  },
                                function(data) {
                                   //alert(JSON.stringify(data))
                                   //var tab_id = data['tab_id'];
                                   var tab_name = data['tab_name'];
                                   //alert(name)
                                   obj.getSavedBtn(tab_id, tab_name)
                               })

                          }
                    };

                 obj.getSavedBtn(tab_id, tab_name)


               }.bind(obj = self)

    div_.setAttribute("style", "background-color: "+ color + "; height: 400px; width: 700px; border: 1px solid black; position: absolute; border-top-left-radius: 10px; border-top-right-radius: 10px;");
    div_.setAttribute("id", "elms_" + tab_id);

    div_move.innerHTML = "Drag and Drop";
    div_move.setAttribute("style", "text-align: center; width: 700px; height: 20px; position: absolute; cursor: move; z-index:10; border-top-left-radius: 10px; border-top-right-radius: 10px; background-color: #2196F3; color: #fff;")

    div_elms.setAttribute("style", "background-color:white; z-index:10; width:700px; height:40px; margin-top:20px; position: absolute; ");
        // CREATING ELEMENTS INSIDE DIV_ELMS

        btn_cp.innerHTML = 'Button2';
        //btn_cp.setAttribute('class', 'small_button');
        div_elms.appendChild(btn_cp);


        // Draggable window
        var pos1=0; pos2=0; pos3=0; pos4=0;
        div_move.onmousedown = function(e) {
                   // calculate mouse coordinates
            pos1 = e.clientX;
            pos2 = e.clientY;

            // calculate position of the mouse
            document.onmousemove = function(e) {
                pos3 = pos1 - e.clientX;
                pos4 = pos2 - e.clientY;

                pos1 = e.clientX;
                pos2 = e.clientY;

                div_.style.left = (div_.offsetLeft - pos3) + "px";
                div_.style.top = (div_.offsetTop - pos4) + "px";

                }

            div_move.onmouseup = function (e) {
                document.onmousemove = null;
                document.onmouseup = null;
            };
            }

            div_edit.setAttribute("style", "background-color: "+ color + "; border: 1px solid black; height: 350px; width: 698px; margin-top: 60px; position: absolute; border-bottom-left-radius: 10px; border-bottom-right-radius: 10px")


             var div_left = document.createElement('div');
            div_left.setAttribute("id", "left_div_" + tab_id);
            //div_left.innerHTML = 'Div_left';
            div_left.setAttribute("style", "background-color: " + color + "; margin-left: -1px; height: 350px; width: 230px; position: absolute; border-bottom-left-radius: 10px;");
            div_left.setAttribute("class", "tabcontent");
            //div_left.style.display = "none";


            //div_right.style.display = "none";
            var div_right = document.createElement('div');
            div_right.setAttribute("id", "right_div_" + tab_id);
            div_right.setAttribute("class", "tabcontent");
            div_right.setAttribute("style", "background-color: "+ color + "; border: 1px solid black; margin-left: 463px; margin-top: -1px; height: 350px; width: 235px; position: absolute; border-bottom-right-radius: 10px")
            txt_area.setAttribute("style", "height: 347px; margin-top: -1px; width: 240px; margin-left: 225px; position: absolute; border-bottom-right-radius: 10px; border-bottom-left-radius: 10px;")

            div_.appendChild(div_move);
            div_.appendChild(div_elms);
            div_.appendChild(div_edit);
            div_edit.appendChild(div_left);
            div_edit.appendChild(div_right);
            div_edit.appendChild(txt_area);



div_btn.appendChild(button_);
this.body_id.appendChild(div_btn);

var div_cp = document.createElement('div');
    div_cp.setAttribute('style', "width:600px; height:400px; background-color:lightgray; position:absolute; left:600px; border-radius: 5px;");
    div_cp.setAttribute('id', 'cp_' + tab_id);
    div_cp.setAttribute('class', 'tabcontent');
    div_cp.style.display = "none";

   div_cp_main.appendChild(div_cp);

div_cp_main.setAttribute('id', 'div_cp_main');
this.body_id.appendChild(div_cp_main);

//DIV THAT HOLDS THE TEXTAREA
 div_txt.setAttribute('id', 'div_txt_');

    var txt = document.createElement("textarea");
            txt.setAttribute("id", "txt_" + tab_id);
            txt.setAttribute("cols", "35");
            txt.setAttribute("rows", "20");
            txt.setAttribute("class", "tabcontent");
            txt.style.display = "none"
            txt.innerHTML += '\n' + description + '\n' + '\n';
            txt.innerHTML += tab_name;

            txt.onchange = function(event) {
                var saved_content = document.getElementById('txt_' + tab_id);
                var updated_content = saved_content.value;
                $.post(self.save_url, {
                    'tab_id': tab_id,
                    'dic_': updated_content,
                }, function(data) {
                }.bind(self));
            };

            div_txt.appendChild(txt);

 this.body_id.appendChild(div_txt);
 this.body_id.appendChild(div_);

 var btn__ = document.querySelectorAll('.tablinks');
 if ( btn__.length > 0) {
    btn__[0].click();
}

  self.getSavedBtn(tab_id, tab_name)
};
// GET DATA
Admin.prototype.get_data = function(event) {
    var self = this;
    //alert(333);
    $.post(self.get_data_url, {}, function(dic) {
        for (var d in dic) {
            var tab_id = d;
            var tab_name = dic[d]['city_name'];
            var description = dic[d]['description'];
            var color = dic[d]['color'];
            var save_btn = dic[d]['save_btn']
            self.create_tab(tab_id, tab_name, description, color, save_btn);
        }
    }.bind(self));
};

var left_btn = document.createElement('button');
Admin.prototype.getSavedBtn = function(tab_id, tab_name) {
    var self = this;
     $.post(self.saved_btn,
        {}, function(data) {
        var btn_data = data['saved_btn_']

        for (var b in btn_data){
            if (b==tab_id){
            var tab_id_btn = btn_data[b];
                for (var t in tab_id_btn){
                    var list_dic = tab_id_btn[t];
                        var d = document.getElementById('cp_'+tab_id);
                        d.innerHTML = '';
                        for (var i of list_dic){
                           var btn_name = i["tab_" + tab_name];
                           name_btn = btn_name.split('_')[1]

                            var btn_id = i["btn_id"]
                            this.id = btn_id;

                            offsetX = btn_name.split("_")[2]
                            offsetY = btn_name.split("_")[3]

                            var btn__ = document.createElement('button');
                            btn__.setAttribute('class','small_button');
                            btn_.setAttribute('id', 'btn_id' + btn_id);
                            btn__.style.position = "absolute";
                            btn__.style.left = offsetX + "px";
                            btn__.style.top = offsetY + "px";
                            btn_.innerHTML = 'button' + name_btn;

                            d.appendChild(btn__);

                            btn__.onclick = function(event){
                                alert(1111)
                                var new_id = event.target;
                                var id_btn = new_id.getAttribute("id");
                                var id_btn_inner = id_btn.split('_')[2];

                                    if (event.shiftKey){
                                         var btn_left = document.getElementById('div_left_' + tab_id);
                                         left_btn.innerHTML = 'onclick_' + id_btn_inner;
                                         left_btn.setAttribute('class','small_button')
                                         left_btn.setAttribute('id', 'onclick' + id_btn_inner);
                                         btn_left.appendChild(left_btn)


                                         var txt_btn = document.createElement('textarea');
                                         txt_btn.setAttribute('style', "height: 347px; margin-top: -1px; width: 240px; margin-left: 225px; position: absolute; border-bottom-right-radius: 10px; border-bottom-left-radius: 10px; background-color: red;")
                                         txt_btn.setAttribute('id', "txt_area_" + tab_name + '_' + id_btn_inner);
                                         txt_btn.setAttribute('class', 'tabcontent');
//                                         txt_area.appendChild(txt_btn);
//                                         div_edit.appendChild(txt_area);  // ?????????????

                                         var tabcontent_ = document.getElementsByClassName('tabcontent');
                                            for (var i = 0; i < tabcontent_.length; i++) {
                                                tabcontent_[i].style.display = "none";
                                            }
                                            document.getElementById('txt_area_' + tab_name + '_' + id_btn_inner).style.display = 'block';
                                    }

                                }
                        }

                }

            }
        }

    }.bind(self));

}