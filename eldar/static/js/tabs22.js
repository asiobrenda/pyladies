function Admin(dic){
//alert(5555)
  //alert(JSON.stringify(dic))

}

Admin.prototype.create_elements = function(dic){
       this.body_id = dic['body_id_'];
       this.add_tab_url = dic['add_tab_url_'];
       this.get_data_url = dic['get_data_'];
       this.delete_tab_url = dic['delete_tab_'];
       this.save_content = dic['save_content_'];
       this.save_btn_ = dic['save_btn_'];
       this.saved_btn_ = dic['saved_btn_'];
       //alert(this.saved_btn_)
       //alert(6666)
       //alert(this.get_data_url);
       this.tabs();
       this.get_data();
       //this.create_tab();
       this.clear_deleted();
}


Admin.prototype.tabs = function(dic){

       function create_id(){
              var counter = 0;

              function gen_id(){
                       return ++counter;
              }
              gen_id()
       }
       create_id()


        var self = this;
        var addtab = document.createElement('button');
         addtab.innerHTML = 'Add Tab';
         addtab.onclick = function(event){
             //alert(1111)
             var tab_name = prompt("Enter tab name").toLowerCase();
             if(!tab_name){alert("must enter tab name");return};
             //alert(tab_name)
             dic = {'city_name': tab_name, 'description': 'Add any city name', 'color': 'blue'};
             $.post(self.add_tab_url,
                 {
                     'dic_':JSON.stringify(dic)
                 },
                 function(data){
                    //alert(JSON.stringify(data));
                    var tab_id = data['tab_id'];
                    var name = data['tab_name'];
                    var color = data['tab_color'];
                    var description = data['tab_content'];
                    self.create_tab(tab_id, name, description, color);
               }
               );
        }.bind(self)

        var delete_tab = document.createElement('button');
        delete_tab.innerHTML = 'Delete Tab';
        delete_tab.onclick = function(event){
                            var delTab = prompt("Enter city name to delete");
                            if (!delTab){alert('Please enter city name'); return};
                            $.post(self.delete_tab_url,
                            {
                                'delete_tab_': delTab
                            },
                            function(data){
                                var button_id = data['tab_id_']
                                self.clear_deleted(button_id)
                                }.bind(self)
                            );
                        }







         var div = document.createElement('div');
          div.setAttribute("style", "margin-left:30px")
         div.appendChild(addtab);
         div.appendChild(delete_tab);

        this.body_id.appendChild(div);

}


//CREATING BUTTONS


var div = document.createElement("div");
var div_txt = document.createElement("div");
var div_pop_up = document.createElement("div");
var div_move = document.createElement("div");
var div_elms = document.createElement("div");
var btn = document.createElement("button");
var div_elements_div = document.createElement("div");
var div_editable = document.createElement("div_editable");



Admin.prototype.create_tab =  function(tab_id, name, description, color){
     var self = this;
    div.setAttribute("style", "margin-left:30px")
//CREATING THE BUTTONS
    var button_ = document.createElement("button");
    button_.setAttribute("class", "tablinks");
    button_.setAttribute("tab_id", tab_id);
    button_.setAttribute("id", 'btn_' + tab_id);
    button_.innerHTML = name;
    button_.onclick = function(event){
              var event = event.target;
              var tab_id = event.getAttribute('tab_id');
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


              function create_id(){
                       self.id = tab_id;
                       //alert(self.id)

                       return function(){
                             return ++self.id;
                       }
              }
              var getId = create_id()
              //alert(getId)



                       btn.onclick = function(event){
                             var evt = event.target;
                             //alert(evt.outerHTML)
                             var copied_btn = evt.cloneNode(true);
                             //alert(copied_btn.outerHTML)
                              document.getElementById("div_elements_" + tab_id ).onclick = function(event){
                                     function genId(){
                                             return getId()
                                     }
                                     var id = genId()
                                     //div_elements.appendChild(copied_btn)
                                      var offsetX = event.offsetX;
                                      //alert(offsetX)
                                      var offsetY = event.offsetY;

                                      copied_btn.style.position = "absolute";
                                      copied_btn.style.left = offsetX + "px";
                                      copied_btn.style.top = offsetY + "px";
                                      copied_btn.setAttribute("id", "btn_" + id);
                                      copied_btn.innerHTML = "button_" + id +'_'+offsetX+'_'+offsetY;
                                      document.getElementById("div_elements_" + tab_id ).appendChild(copied_btn);
                                      document.getElementById("div_elements_" + tab_id ).onclick = null;

                                        var save_btn = copied_btn.innerHTML;
                                       //alert(save_btn.innerHTML)
                                       //alert(3333)
                                       //alert(self.save_btn)
                                       $.post(self.save_btn_,
                                         {
                                             'tab_num': tab_id,
                                             'tab_name': name,
                                             'save_btn1_': save_btn,
                                             'btn_id': id
                                         },
                                         function(data){}
                                  );
                              };
                             }

                 $.post(self.saved_btn_,
                                {},
                                function(data){
                                   //alert(JSON.stringify(data))
                                   var btn_data = data['saved_btn'];
                                   //alert(JSON.stringify(btn_data))
                                   for (var b in btn_data){
                                   if (b == tab_id){
                                        var tab_id_btn = btn_data[b];
                                        //alert(JSON.stringify(tab_id_btn))
                                        for (var t in tab_id_btn){
                                           var list_dic = tab_id_btn[t];
                                           //alert(JSON.stringify(list_dic))
                                            var d = document.getElementById('div_elements_'+tab_id);
                                            d.innerHTML = '';
                                           for (var elt of list_dic){
                                            var btn_ = document.createElement('button');
                                               for(var btn_name in elt){
                                                    var btn__ = elt["btn_" + name];
                                                    //alert(btn__)
                                                    var btn_id = elt["btn_id_"]
                                                    this.id = btn_id;
                                                    var btn_name_ = btn__.split('_')[0]
                                                    //alert(btn__)
                                                    //var btn_name_ = btn__.split('_')[1]
                                                    //alert(btn_name_)
                                                    offsetX = btn__.split('_')[2]
                                                    //alert(1111)
                                                    //alert(offsetX)
                                                    offsetY = btn__.split('_')[3]
                                                    //alert(offsetY)
                                                    btn_.style.position = "absolute";
                                                    btn_.style.left = offsetX + "px";
                                                    btn_.style.top = offsetY + "px";
                                                    btn_.setAttribute("id", "btn_"+btn_id);

                                                    btn_.innerHTML = btn_name_;
                                                    //alert(22222)
                                                    d.appendChild(btn_);

                                                        btn_.onclick = function(event){
                                                             //alert(1111)
                                                             //alert(btn_id)
                                                             var event_ = event.target;
                                                             //alert(event_.outerHTML)
                                                             var id_ = event_.getAttribute('id');
                                                             alert(id_)
                                                             var btn_id_ = id_.split('_')[1]
                                                             //alert(btn_id_)
                                                             if (event.ctrlKey){
                                                                 alert(333333)
                                                                 var div_left_ = document.getElementById('left_div_' + tab_id);
                                                                 alert(div_left_.outerHTML)

                                                             }



                                                        }

                                               }

                                           }


                                        }


                                   }
                                   }
                                }.bind(self)
                            )


            document.getElementById("txt_" + tab_id).style.display = "block";
            document.getElementById("div_elements_" + tab_id ).style.display = "block";
            document.getElementById("left_div_" + tab_id ).style.display = "block";
            document.getElementById("right_div_" + tab_id ).style.display = "block";
            document.getElementById("txt_div_" + tab_id ).style.display = "block";
            event.currentTarget.className += " active";

            }.bind(self)




                //CREATING DRAGGABLE DIV

                    div_pop_up.setAttribute("style", "height:500px; width:700px; background-color:LightGray;position:absolute; top:300px");
                    div_pop_up.setAttribute("id", 'elms_'+tab_id);

                    div_move.setAttribute("style", "padding: 10px; cursor: move; z-index:10; background-color: #2196F3; color: #fff; text-align:center")
                    div_move.innerHTML = "Click here to move me";


                    //CREATING DIV THAT HAS ALL ELEMENTS

                       div_elms.setAttribute("style", "background-color:white; z-index:10; height:60px; width:700px");

                       //CREATING ELEMENTS INSIDE DIV_ELMS
                       btn.setAttribute("style", "margin-left:10px; margin-top:3px")
                       div_elms.appendChild(btn);

                    //CREATING DIV THAT WILL BE EDITABLE
                     div_editable.setAttribute("style", "background-color:LightGray; height:400px; width:700px; position:absolute");
                     //div_editable.setAttribute("id", 'editable_' + tab_id)

                     //CREATING THE LEFT DIV
                      var left_div = document.createElement('div');
                      left_div.setAttribute("style", "background-color:LightGray; width:230px; height:400px; border-color:LightGray; border-style:solid");
                      left_div.setAttribute("id", 'left_div_' + tab_id);
                      left_div.setAttribute("class", 'tabcontent');
                      left_div.innerHTML = "left_div";


                      //CREATING TEXTAREA
                      var txt_div = document.createElement('textarea');
                      txt_div.setAttribute("style", "width:215px; height:400px; margin-left:226px; margin-top:-415px; margin-bottom:20px");
                      txt_div.setAttribute("id", 'txt_div_' + tab_id);
                      txt_div.setAttribute("class", 'tabcontent');
                      txt_div.innerHTML = "textarea";

                      //CREATING RIGHT DIV
                      var right_div = document.createElement('div');
                      right_div.setAttribute("style", "background-color:LightGray; width:210px; height:400px; margin-left:465px; margin-top:-435px; border-color:LightGray; border-style:solid");
                      right_div.setAttribute("id", 'right_div_' + tab_id);
                      right_div.setAttribute("class", 'tabcontent');
                      right_div.innerHTML = "right_div";


                       div_editable.appendChild(left_div);
                       div_editable.appendChild(txt_div);
                       div_editable.appendChild(right_div);



                    var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
                                 //Use the 3 events
                                 div_move.onmousedown = function(e){
                                      pos1 = e.clientX;
                                      pos2 = e.clientY;

                                      document.onmousemove = function(e){
                                               pos3 = pos1 - e.clientX;
                                               pos4 = pos2 - e.clientY;


                                               pos1 = e.clientX;
                                               pos2 = e.clientY;

                                 div_pop_up.style.left = (div_pop_up.offsetLeft - pos3) + 'px';
                                 div_pop_up.style.top = (div_pop_up.offsetTop - pos4) + 'px';


                                      };
                                 div_move.onmouseup = function(e){
                                         document.onmousemove = null;
                                         document.onmousedown = null;
                                 };
                                 };

                                  div_pop_up.appendChild(div_move);
                                 div_pop_up.appendChild(div_elms);
                                 div_pop_up.appendChild(div_editable);



    div.appendChild(button_)
    this.body_id.appendChild(div);

       //CREATING DIV WHERE ELEMENTS WILL BE COPIED/PASTED

         div_elements_div.setAttribute("id", "div_elements_div")
         var div_elements = document.createElement("div");
         div_elements.setAttribute("class", "tabcontent");
         div_elements.setAttribute("style", "width:500px; height:450px; background-color:LightPink; position:relative; margin-left:700px");
         div_elements.setAttribute("id", "div_elements_" + tab_id );

         div_elements_div.appendChild(div_elements)
         this.body_id.appendChild(div_elements_div);

          div_txt.setAttribute("style", "margin-left:30px; margin-top:-450px")

                        //CREATING TEXT AREA
                                var txt = document.createElement("textarea");
                                txt.setAttribute("id", "txt_" + tab_id);
                                txt.setAttribute("cols", "35")
                                txt.setAttribute("rows", "20")
                                txt.setAttribute("class", "tabcontent");
                                txt.innerHTML += name + '\n' + '\n' + '\n';
                                txt.innerHTML += '\n' + description + '\n' + '\n' ;
                                //txt.innerHTML += 'color: ' + color;
                                txt.onchange = function(event){
                                //alert(2222)
                                         var content = document.getElementById('txt_' + tab_id);
                                         var txt_content = content.value;
                                         //alert(txt_content)
                                         //var txt_content = txt_content.toLowerCase();
                                         $.post(self.save_content,
                                             {
                                                'tab_id': tab_id,
                                                'dic_':txt_content
                                             },
                                             function(data){
                                             });

                                    }.bind(self)

                                div_txt.appendChild(txt);



        this.body_id.appendChild(div_txt);
        this.body_id.appendChild(div_pop_up);
        btn.innerHTML = "button1";

        div_elms.appendChild(btn);
   }
    // Assuming you have already defined btn and div_elements elsewhere in your code

// Assuming you have already defined btn and div_elements elsewhere in your code
//
//btn.onclick = function(event) {
//    var evt = event.target;
//    var copied_btn = evt.cloneNode(true);
//
//    // Click event handler for div_elements
//    div_elements.onclick = function(event) {
//        var offsetX = event.offsetX;
//        var offsetY = event.offsetY;
//
//        // Set the position of the copied button relative to the container
//        copied_btn.style.position = "absolute";
//        copied_btn.style.left = offsetX + "px";
//        copied_btn.style.top = offsetY + "px";
//
//        // Append the cloned button to the div_elements
//        div_elements.appendChild(copied_btn);
//    };
//};
//
//




//GETTING DATA
Admin.prototype.get_data = function(event) {
    //alert(66666);
    var self = this;
    //alert(self.get_data_url)
    $.post(self.get_data_url, {}, function(dic) {
    //alert(JSON.stringify(dic))
        for (var d in dic) {
            var tab_id = d;
            var name = dic[d]['city_name'];
            var color = dic[d]['tab_color'];
            var description = dic[d]['tab_content'];
            //alert(1111)
            //alert(description)
            self.create_tab(tab_id, name, description, color); // Call create_tab method to create each tab
        }
    }.bind(self))
}

//CLEARING TAB BUTTON
Admin.prototype.clear_deleted = function(button_id){
    var delete_button = document.getElementById('btn_'+ button_id)
    delete_button.outerHTML = '';
    var delete_txt = document.getElementById('txt_'+ button_id)
    delete_txt.outerHTML = '';
};