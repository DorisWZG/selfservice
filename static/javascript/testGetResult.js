function showResult() {
    var table = $("#result-table");
    table.find("tr").slice(1).remove();
    table.addClass("hidden");
    var row1 = $("<tr></tr>");
    $("<td></td>").html("Baidu PPC").appendTo(row1);
    $("<td></td>").html("$1000").appendTo(row1);
    $("<td></td>").html("3000").appendTo(row1);
    $("<td></td>").html("$0.68").appendTo(row1);
    $("<td></td>").html("680,000").appendTo(row1);
    $("<td></td>").html("$2.2").appendTo(row1);
    table.append(row1).removeClass("hidden");
}
$.ajax({
        url: siteUrl + "/restapi/industry_list",
        method: "GET",
        headers: { "Accept": "application/json; odata=verbose" },
        success: function (data) {
           console.log(JSON.stringify(data.d.results));
        },
        error: function (data) {
           console.log(JSON.stringify(data));
        }
});