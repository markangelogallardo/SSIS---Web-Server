$(document).ready(function(){
  $("#search").on("keyup", function() {
    var field = $("#fields").val()
    var value = $(this).val().toLowerCase();
    $("#details tr").each(function() {
      let matchColumn = true;
      if (value !== "") {
          let columnData = $(this).find("td:nth-child(" +
              (field === "ID Number" ? 1 :
                  (field === "First Name" ? 2 : 
                    (field === "Last Name" ? 3 : 
                      (field === "Program Code" ? 4 : 
                        (field === "Year Level" ? 5 : 
                          (field === "Gender" ? 6 : 7)))))) +
              ")").text().toLowerCase();
          matchColumn = columnData.indexOf(value) > -1;
      }

      $(this).toggle(matchColumn);
          //$(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    })
  });
  
    
});



  