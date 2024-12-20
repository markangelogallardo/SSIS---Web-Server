$(document).ready(function(){
  $("#search").on("keyup", function() {
    var field = $("#stud_fields").val()
    var value = $(this).val().toLowerCase();
    $("#details tr").each(function() {
      let matchColumn = true;
      if (value !== "") {
          let columnData = $(this).find("td:nth-child(" +
              (field === "ID Number" ? 2 :
                  (field === "First Name" ? 3 : 
                    (field === "Last Name" ? 4 : 
                      (field === "Program Code" ? 5 : 
                        (field === "Year Level" ? 6 : 
                          (field === "Gender" ? 7 : 8)))))) +
              ")").text().toLowerCase();
          matchColumn = columnData.indexOf(value) > -1;
      }

      $(this).toggle(matchColumn);
    })
  });
  
    
});



  