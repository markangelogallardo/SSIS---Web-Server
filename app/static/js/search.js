
function myFunction(){

    var tr, td, text, i, j, filter;


    input = document.getElementById("studentSearch");
    filter = input.value.toUpperCase();
    tbody = document.getElementById("studDeats");
    tr = tbody.getElementsByTagName("tr");

    //td = tr[0].getElementsByTagName("td");
    
    //console.log(tr)
    
    for(i=0; i < tr.length; i++){
        for(j=0;j<6;j++){
            td = tr[i].getElementsByTagName("td")[j];
            text = td.textContent || td.innerText;
            if (text.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
                console.log(text)   
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

$('button').change(function(){
    $('#dropdownMenuButton').val();
 });



//console.log(tr);


/*function myFunction() {
    var input, filter, tr, td, a, i, txtValue;
    input = document.getElementById("studentSearch");
    filter = input.value.toUpperCase();
    tr = document.getElementById("studDeats");
    td = tr.getElementsByTagName("td");
    for (i = 0; i < tr.length; i++) {
        for(j=0; j < tr[i].length; j++) {
            txtValue = a.textContent || a.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                li[i].style.display = "";
            } else {
                li[i].style.display = "none";
            }
        }

}*/