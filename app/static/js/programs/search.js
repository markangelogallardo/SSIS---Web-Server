$(document).ready(function(){
  $("#search").on("keyup", function() {
    var field = $("#prog_fields").val()
    var value = $(this).val().toLowerCase();
    $("#details tr").each(function() {
      let matchColumn = true;
      if (value !== "") {
          let columnData = $(this).find("td:nth-child(" +
              (field === "Program Code" ? 1 :
                  (field === "Program Name" ? 2 : 
                    (field === "College Code" ? 3 : 4 ))) +
              ")").text().toLowerCase();
          matchColumn = columnData.indexOf(value) > -1;
      }

      $(this).toggle(matchColumn);
          //$(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    })
  });
  
    
});



  