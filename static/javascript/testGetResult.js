function check_submit() {
    var category = $("#selectCategory").val();
    var budget = $("#selectBudget").val();
     if (budget != "" && category != "") {
        $('input[type="submit"]').removeClass('disabled');
     }
     else $('input[type="submit"]').addClass();
//    if ($(this).val().length == 0) {
//        $(":submit").attr("disabled", true);
//    } else {
//        $(":submit").removeAttr("disabled");
//    }
}
function showResult() {
    $("#submit").attr('disabled','disabled');
    var category = $("#selectCategory").val();

    var budget = $("#selectBudget").val();
    if (budget != "" && category != "") {
        $('input[type="submit"]').removeAttr('disabled');
    }
    var url = "/budget_allocation/metrics_result/industry/" + category + "/budget/" + budget;
    $.get(url).done(function(data) {
        var table = $("#result-table");
        table.find("tr").slice(1).remove();
        table.addClass("hidden");
        $(data).each(function(idx, value) {
            var row = $("<tr></tr>");
            $("<td></td>").html(value["channelName"]).appendTo(row);
            $("<td></td>").html(value["allocation"]).appendTo(row);
            $("<td></td>").html(value["expectedClicks"]).appendTo(row);
            $("<td></td>").html(value["costPerClick"]).appendTo(row);
            $("<td></td>").html(value["expectedImpressions"]).appendTo(row);
            $("<td></td>").html(value["costPerImpression"]).appendTo(row);
            row.appendTo(table);
        });
        table.removeClass("hidden");
    }).fail(function(data) {
        alert("Status Code: " + data.status + ", Status Text: " + data.statusText + ", Response Text: " + data.responseText);
    });

}
//$.ajax({
//        url: siteUrl + "/restapi/industry_list",
//        method: "GET",
//        headers: { "Accept": "application/json; odata=verbose" },
//        success: function (data) {
//           console.log(JSON.stringify(data.d.results));
//        },
//        error: function (data) {
//           console.log(JSON.stringify(data));
//        }
//});