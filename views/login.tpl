<!DOCTYPE html>
<html>
<head>
    <!-- <link rel="stylesheet" href="/static/style.css" type="text/css" media="screen" /> -->
    <link href="/static/css/bootstrap.min.css" rel="stylesheet" media="screen">
    
    <style type="text/css">
      body {
        padding-top: 40px;
        padding-bottom: 40px;
        background-color: #f5f5f5;
      }
            .form-signin {
        max-width: 300px;
        padding: 19px 29px 29px;
        margin: 0 auto 20px;
        background-color: #fff;
        border: 1px solid #e5e5e5;
      }
      .form-signin .form-signin-heading,
      .form-signin {
        margin-bottom: 10px;
      }
      .form-signin input[type="text"],
      .form-signin input[type="password"] {
        font-size: 16px;
        height: auto;
        margin-bottom: 15px;
        padding: 7px 9px;
      }
      </style>
</head>
<body>
    <div class="container">
    	<form method="post" id="form" action="/admin/login" class="form-signin">
    		<h2 class="form-signin-heading">Please sign in</h2>
        %if error:
    		<h4 class="text-error">Wrong password try again</h2>
    	%end
      <input type="text" name="username"  placeholder="Login name" /><br/>
      <input type="password" name="password"  placeholder="Password" /><br/>
      <button type="submit"  class="btn  btn-large btn-primary">Login</button>
   </form>
   </div>
</body>
</html>