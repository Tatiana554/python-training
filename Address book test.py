{
  "id": "5ea40a29-10a1-4526-aa02-7a82b5a6dd14",
  "version": "2.0",
  "name": "Address book test",
  "url": "http://localhost",
  "tests": [{
    "id": "dc387a7a-7c6f-4670-98d4-fc55dde1d9fc",
    "name": "New group address book",
    "commands": [{
      "id": "c2b6ba3a-3f7e-44f6-a6c5-8a196f2e735b",
      "comment": "",
      "command": "open",
      "target": "/addressbook/group.php",
      "targets": [],
      "value": ""
    }, {
      "id": "c29f430f-fb56-4da1-a787-7c9a667e6d66",
      "comment": "",
      "command": "setWindowSize",
      "target": "1162x834",
      "targets": [],
      "value": ""
    }, {
      "id": "a85785c4-7393-4f18-9124-48509d00a0bb",
      "comment": "",
      "command": "click",
      "target": "id=LoginForm",
      "targets": [
        ["id=LoginForm", "id"],
        ["name=LoginForm", "name"],
        ["css=#LoginForm", "css:finder"],
        ["xpath=//form[@id='LoginForm']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form", "xpath:idRelative"],
        ["xpath=//form", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "62445fd3-44e4-4cfa-a696-7412958f635e",
      "comment": "",
      "command": "click",
      "target": "name=pass",
      "targets": [
        ["name=pass", "name"],
        ["css=input:nth-child(5)", "css:finder"],
        ["xpath=//input[@name='pass']", "xpath:attributes"],
        ["xpath=//form[@id='LoginForm']/input[2]", "xpath:idRelative"],
        ["xpath=//input[2]", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "803b3cc8-5de6-4c31-89d4-001a3422cd2c",
      "comment": "",
      "command": "type",
      "target": "name=pass",
      "targets": [
        ["name=pass", "name"],
        ["css=input:nth-child(5)", "css:finder"],
        ["xpath=//input[@name='pass']", "xpath:attributes"],
        ["xpath=//form[@id='LoginForm']/input[2]", "xpath:idRelative"],
        ["xpath=//input[2]", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "eb0ffab3-e2c2-423f-a860-5ca4032b7b38",
      "comment": "",
      "command": "click",
      "target": "name=user",
      "targets": [
        ["name=user", "name"],
        ["css=input:nth-child(2)", "css:finder"],
        ["xpath=//input[@name='user']", "xpath:attributes"],
        ["xpath=//form[@id='LoginForm']/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "eec53b5d-14b7-4d7f-807a-cc0b6cebcf63",
      "comment": "",
      "command": "type",
      "target": "name=user",
      "targets": [
        ["name=user", "name"],
        ["css=input:nth-child(2)", "css:finder"],
        ["xpath=//input[@name='user']", "xpath:attributes"],
        ["xpath=//form[@id='LoginForm']/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "admin"
    }, {
      "id": "8e8c762d-f85e-4759-917a-5baa0ed8c1ca",
      "comment": "",
      "command": "type",
      "target": "name=pass",
      "targets": [
        ["name=pass", "name"],
        ["css=input:nth-child(5)", "css:finder"],
        ["xpath=//input[@name='pass']", "xpath:attributes"],
        ["xpath=//form[@id='LoginForm']/input[2]", "xpath:idRelative"],
        ["xpath=//input[2]", "xpath:position"]
      ],
      "value": "secret"
    }, {
      "id": "2fa8fa0c-93a6-4cfc-9f73-16314c73a009",
      "comment": "",
      "command": "click",
      "target": "css=input:nth-child(7)",
      "targets": [
        ["css=input:nth-child(7)", "css:finder"],
        ["xpath=//input[@value='Login']", "xpath:attributes"],
        ["xpath=//form[@id='LoginForm']/input[3]", "xpath:idRelative"],
        ["xpath=//input[3]", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "d387e5d1-4861-4355-81e9-7898f74027c6",
      "comment": "",
      "command": "click",
      "target": "name=selected[]",
      "targets": [
        ["name=selected[]", "name"],
        ["css=.group:nth-child(5) > input", "css:finder"],
        ["xpath=//input[@name='selected[]']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form/span/input", "xpath:idRelative"],
        ["xpath=//span/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "fb500623-6507-4698-9dd8-238dec33192c",
      "comment": "",
      "command": "click",
      "target": "name=selected[]",
      "targets": [
        ["name=selected[]", "name"],
        ["css=.group:nth-child(5) > input", "css:finder"],
        ["xpath=//input[@name='selected[]']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form/span/input", "xpath:idRelative"],
        ["xpath=//span/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "9cd0d98c-0087-4bd6-864f-560aa10a5cc6",
      "comment": "",
      "command": "click",
      "target": "name=new",
      "targets": [
        ["name=new", "name"],
        ["css=form:nth-child(2) > input:nth-child(1)", "css:finder"],
        ["xpath=//input[@name='new']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form/input", "xpath:idRelative"],
        ["xpath=//div[4]/form/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "6ae4994b-dc75-4c73-bbbf-5f80898c1aa1",
      "comment": "",
      "command": "click",
      "target": "name=group_name",
      "targets": [
        ["name=group_name", "name"],
        ["css=input:nth-child(2)", "css:finder"],
        ["xpath=//input[@name='group_name']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form/input", "xpath:idRelative"],
        ["xpath=//div[4]/form/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "06ab69ea-a6bc-4df7-8cff-f88516ebf100",
      "comment": "",
      "command": "type",
      "target": "name=group_name",
      "targets": [
        ["name=group_name", "name"],
        ["css=input:nth-child(2)", "css:finder"],
        ["xpath=//input[@name='group_name']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form/input", "xpath:idRelative"],
        ["xpath=//div[4]/form/input", "xpath:position"]
      ],
      "value": "group 3"
    }, {
      "id": "60409cbe-10f7-484f-b4e8-33495118d872",
      "comment": "",
      "command": "click",
      "target": "name=group_header",
      "targets": [
        ["name=group_header", "name"],
        ["css=textarea:nth-child(9)", "css:finder"],
        ["xpath=//textarea[@name='group_header']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form/textarea", "xpath:idRelative"],
        ["xpath=//textarea", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "48c26ff4-83c3-4b7f-9db7-ed207f4fdb39",
      "comment": "",
      "command": "type",
      "target": "name=group_header",
      "targets": [
        ["name=group_header", "name"],
        ["css=textarea:nth-child(9)", "css:finder"],
        ["xpath=//textarea[@name='group_header']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form/textarea", "xpath:idRelative"],
        ["xpath=//textarea", "xpath:position"]
      ],
      "value": "test"
    }, {
      "id": "22e4163a-bcb4-4ce8-8bac-4beadc130574",
      "comment": "",
      "command": "type",
      "target": "name=group_footer",
      "targets": [
        ["name=group_footer", "name"],
        ["css=textarea:nth-child(12)", "css:finder"],
        ["xpath=//textarea[@name='group_footer']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form/textarea[2]", "xpath:idRelative"],
        ["xpath=//textarea[2]", "xpath:position"]
      ],
      "value": "test"
    }, {
      "id": "5b1f0597-09c1-42ee-a3d9-64a2ae5914d3",
      "comment": "",
      "command": "click",
      "target": "name=submit",
      "targets": [
        ["name=submit", "name"],
        ["css=input:nth-child(15)", "css:finder"],
        ["xpath=//input[@name='submit']", "xpath:attributes"],
        ["xpath=//div[@id='content']/form/input[2]", "xpath:idRelative"],
        ["xpath=//input[2]", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "0bda4f2e-bf50-453a-a1ee-8b94ddb56589",
      "comment": "",
      "command": "click",
      "target": "linkText=group page",
      "targets": [
        ["linkText=group page", "linkText"],
        ["css=i > a", "css:finder"],
        ["xpath=//a[contains(text(),'group page')]", "xpath:link"],
        ["xpath=//div[@id='content']/div/i/a", "xpath:idRelative"],
        ["xpath=(//a[contains(@href, 'group.php')])[2]", "xpath:href"],
        ["xpath=//i/a", "xpath:position"],
        ["xpath=//a[contains(.,'group page')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "13fed6ed-90bf-4b77-b685-47e7ccb2e4e4",
      "comment": "",
      "command": "click",
      "target": "linkText=Logout",
      "targets": [
        ["linkText=Logout", "linkText"],
        ["css=a:nth-child(3)", "css:finder"],
        ["xpath=//a[contains(text(),'Logout')]", "xpath:link"],
        ["xpath=//a[@onclick='document.logout.submit();']", "xpath:attributes"],
        ["xpath=//div[@id='top']/form/a", "xpath:idRelative"],
        ["xpath=//a[contains(@href, '#')]", "xpath:href"],
        ["xpath=//a", "xpath:position"],
        ["xpath=//a[contains(.,'Logout')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "b6022477-7698-41b9-a2ec-9baca7a0e3f3",
      "comment": "",
      "command": "type",
      "target": "name=user",
      "targets": [
        ["name=user", "name"],
        ["css=input:nth-child(2)", "css:finder"],
        ["xpath=//input[@name='user']", "xpath:attributes"],
        ["xpath=//form[@id='LoginForm']/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "admin"
    }]
  }],
  "suites": [{
    "id": "8390eac2-c7b0-4fc9-a834-d3e16cfdafcd",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["dc387a7a-7c6f-4670-98d4-fc55dde1d9fc"]
  }],
  "urls": ["http://localhost/"],
  "plugins": []
}