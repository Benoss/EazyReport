<!DOCTYPE html>
<html>
<head>
    %include('minitemplate/css', css_list=page.css)
    <style type="text/css"> </style>
    %include('minitemplate/js', js_list=page.head_js)
</head>
<body>
<div class="navbar navbar-inverse navbar-fixed-top">
  <div class="container">
    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".nav-collapse">
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
    </button>
    <a class="navbar-brand" href="#">{{ page.get_config().app_name }}</a>
    <div class="nav">
      <ul class="nav navbar-nav">
        %for link in page.get_menu(1):
        <li class="{{  link.is_selected(page.get_path(), 'selected') }}"><a href="{{ link.get_path() }}">{{ link.get_name() }}</a></li>
        %end
      </ul>
    </div><!--/.nav-collapse -->
  </div>
</div>
<div class="container">
	%include(page.main_template, page=page)
</div>
    %include('minitemplate/js', js_list=page.foot_js)
    %for template in page.foot_js_templates:
        %include(template.template, content = template.content)
    %end

</body>
</html>