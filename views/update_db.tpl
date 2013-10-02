<div class="col-md-2">
 <div class="bs-sidebar">
   <ul class="nav bs-sidenav">       
   %for model in page.model_list:    
       <li>
         <a href="?table={{ model }}">{{ model }}</a>
       </li>
    %end
     </ul>
   </div>
 </div>
 <div class="col-md-10" role="main">

%if page.rows:
<table class="table table-striped">
        <thead>
          <tr>
          %for name in page.table_fields_name:
           <th>{{ name }}</th>
          %end
          </tr>
        </thead>
        <tbody>
        %for row in page.rows:
          <tr>
           %for index, val in enumerate(row):
             %if index == 0:
                <td><a href='?table={{page.table}}&action=edit&id={{val}}'>Edit {{val}}</a></td>
              %else:
                <td>{{ val }}</td>
              %end
            %end
          </tr>
         %end
        </tbody>
      </table>
          <div class="col-lg-offset-2 col-lg-10">
  <a href='?table={{page.table}}&action=create' class="btn btn-primary btn-lg">Create Record</a>
    </div>
%elif len(page.table_fields) > 0:
   <form class="form-horizontal" role="form" method='post'>
   %for name, field in page.table_fields.iteritems():  
    <div class="form-group">
    <input type="hidden" name="table" value="{{page.table}}" />
   <input type="hidden" name="action" value="update" />
      <label for="{{ field.name }}" class="col-lg-2 control-label">{{ name }}</label>
      <div class="col-lg-10">
      %if field.db_field == 'text':
       <textarea class="form-control" id="{{ field.name }}" name="{{ field.name }}" rows="3">{{ page.values[0][field.name] if hasattr(page, 'values') else ''}}</textarea>
      %elif field.db_field == 'primary_key':
        <input type="text" disabled class="form-control" id="{{ field.name }}" name="{{ field.name }}"  placeholder="AUTO GENERATED" value="{{ page.values[0][field.name] if hasattr(page, 'values') else ''}}">
      %else:
        <input type="text" class="form-control" id="{{ field.name }}" name="{{ field.name }}"  placeholder="{{ field.db_field }}" value="{{ page.values[0][field.name] if hasattr(page, 'values') else ''}}">
      %end
      </div>
    </div>
   %end
     <div class="form-group">
       <div class="col-lg-offset-2 col-lg-10">
      <button type="submit" class="btn btn-primary">Save</button>
    </div>
   </div>
  </form>
%end

 </div>