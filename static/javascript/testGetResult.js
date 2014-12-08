function showResult() {
    var category = $("#selectCategory").val();
    var budget = $("#selectBudget").val();
    var url = "/budget_allocation/metrics_list/industry/" + category + "/budget/" + budget;
    $.get(url).done(function(data) {
        var table = $("#result-table");
        table.find("tr").slice(1).remove();
        table.addClass("hidden");
        $(data).each(function(idx, value) {
            var row = $("<tr></tr>");
            $("<td></td>").html(value["channelID"]).appendTo(row);
            $("<td></td>").html(value["allocation"]).appendTo(row);
            $("<td></td>").html(value["budget"]).appendTo(row);
            $("<td></td>").html(value["costPerClick"]).appendTo(row);
            $("<td></td>").html(value["expectedImpressions"]).appendTo(row);
            $("<td></td>").html(value["costPerImpression"]).appendTo(row);
            row.appendTo(table);
        });
        table.removeClass("hidden");
    }).fail(function(data) {
        alert(data);
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