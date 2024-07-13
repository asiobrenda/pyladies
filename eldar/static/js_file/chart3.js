var chart = 'bars'
var last_pdt_chosen = null;
//alert(last_pdt_chosen)
var clicked_btns = []

function reset_btn_color(){
        for (var i=0; i<clicked_btns.length; i++){
             clicked_btns[i].style.color = 'black';
        }
}

function change_chart_type(event, type){
        //alert(1111)
      reset_btn_color()
      var clicked_btn = event.target;
      //alert(clicked_btn.innerHTML)
      clicked_btn.style.color = "blue";
      clicked_btns.push(clicked_btn);
      chart = type;
      //alert(333333)
      //alert(chart)

     var clickEvent = new Event('click', {bubbles: true});
     if (last_pdt_chosen !== null){
         last_pdt_chosen.dispatchEvent(clickEvent);
     }
}


function get_chart_data(event) {
    // Correct the comment
    //alert(elm)
    var elm = event.target;
    last_pdt_chosen = elm;
    var title = elm.innerHTML;
    var id = elm.getAttribute('id');
    alert(id)
    var data = elm.parentNode;
    var imp = 'imports_' + id.split('_')[1];
    alert(imp)
    var exp = 'exports_' + id.split('_')[1];
    var import_data = [];
    var export_data = [];
    var y = [];

    for (var i = 2015; i < 2020; i++) {
        imports = document.getElementById(imp + '_' + i).innerHTML;
        exports = document.getElementById(exp + '_' + i).innerHTML;
        import_data.push(imports);
        export_data.push(exports);
        y.push(i);
    }
    alert(import_data)
    if (chart == 'bars'){
         get_bars_data(import_data, export_data, y, title)
    }else if (chart == 'lines'){
         get_line_data(import_data, export_data, y, title)
    }
}

function get_line_data(imports, exports, years, title) {
    var importsTrace = {
        x: years,
        y: imports,
        type: 'line',
        name: 'Imports',
    };

    var exportsTrace = {
        x: years,
        y: exports,
        type: 'line',
        name: 'Exports',
    };

    var layout = {
        title: title,
    };

    var data = [importsTrace, exportsTrace];

    Plotly.newPlot('myChart', data, layout);
}


function get_bars_data(imports, exports, years, title) {
var Imports = {
  x: years,
  y: imports,
  name: 'imports',
  type: 'bar'
};

var Exports = {
  x: years,
  y: exports,
  name: 'exports',
  type: 'bar'
};

var data = [Imports, Exports];

 var layout = {
        title: title,
    };

Plotly.newPlot('myChart', data, layout);

}