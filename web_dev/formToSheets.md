# Send Form Data to "Sheets"

### Create a new sheet

### Copy URL

### Extensions -> AppScript
Add the following code:
```js
function doPost(e) {

    // Sheet ID is present in the url identifier
    var ss = SpreadsheetApp.openById("yourSheetId");
    var sheet = ss.getSheetByName("Sheet1"); // Change 'Sheet1' to your sheet name

    var data = JSON.parse(e.postData.contents);

    var name = data.Name;
    var email = data.Email;
    var department = data.Department;
    var year = data.Year;

    sheet.appendRow([name, email, department, year]);

    var response = {
        message: "SUCCESS"
    };

    return ContentService.createTextOutput(JSON.stringify(response)).setMimeType(ContentService.MimeType.JSON);
}
```

In the handleSubmit of Form:
```js
    // Send request and store response
    const response = await fetch(apiURL, {
        method: "POST",
        redirect: "follow",
        headers: {
            "Content-Type": "text/plain;charset=utf-8",
        },
        body: JSON.stringify(userData),
    });
```