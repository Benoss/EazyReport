<div class="col-md-2">
   <ul class="nav  nav-pills nav-stacked">       
   %for report in page.reports:
       <li class='{{page.active(report.name)}}'>
         <a href="?report={{ report.name }}&action=edit">{{ report.name }}</a>
       </li>
    %end
    <li>
    <a href="?action=new">Create New</a>
    </li>
     </ul>
 </div>
 <div class="col-md-10" role="main">
    %if page.action == 'edit':
      
      <form class="form-horizontal" role="form" method='post'>
         <input type="hidden" name="action" value="update" />
        <div class="form-group">
          <label for="report_name" class="col-lg-2 control-label">Report Name</label>
          <div class="col-lg-10">
            <input type="text" class="form-control" id="report_name" name="name"  
                                 placeholder="Report Name" value="{{page.report.name}}" />
          </div>
        </div>
        <div class="form-group">
          <label for="report_description" class="col-lg-2 control-label">Report Description</label>
          <div class="col-lg-10">
            <textarea class="form-control" id="report_description" name="description"  
                      rows="3" >{{page.report.description}}</textarea>
          </div>
        </div>
        <div class="form-group">
          <label for="report_last_rune" class="col-lg-2 control-label">Last Run</label>
          <div class="col-lg-2">
            <input type="text" disabled class="form-control" id="report_last_rune" name="last_run"  
                                 placeholder="Last Run" value="{{page.report.last_run}}" />
          </div>
          <label for="report_nb_rows" class="col-lg-2 control-label">Nb Rows</label>
          <div class="col-lg-2">
            <input type="text" disabled class="form-control" id="report_nb_rows" name="nb_rows"  
                                 placeholder="NB Rows" value="{{page.report.nb_rows}}" />
          </div>
          <label for="report_type" class="col-lg-2 control-label">Report Type</label>
          <div class="col-lg-2">
            <select class="form-control" id="report_type" name="report_type">
                <option value="invisible" {{page.get_type("invisible")}} >Invisible</option>
                <option value="report" {{page.get_type("report")}}>Report</option>
                <option value="sanity" {{page.get_type("sanity")}}>Sanity Check</option>
            </select>

          </div>
        </div>
        <div class="form-group">
          <label for="report_cache_duration" class="col-lg-2 control-label">Cache Duration</label>
          <div class="col-lg-4">
            <input type="text" class="form-control" id="report_cache_duration" name=cache_duration  
                                 placeholder="Cache Duration" value="{{page.report.cache_duration}}" />
          </div>
          <label for="report_last_duration" class="col-lg-2 control-label">Last Durations</label>
          <div class="col-lg-4">
            <input type="text" disabled class="form-control" id="report_last_duration" name="last_duration"  
                                 placeholder="Last Duration" value="{{page.report.last_duration}}" />
          </div>
        </div>
        <div class="form-group">
          <label for="row_callback" class="col-lg-2 control-label">Row Callback</label>
          <div class="col-lg-10">
            <textarea class="form-control" id="row_callback" name="row_callback"  
                      rows="6" >{{page.report.row_callback}}</textarea>
          </div>
        </div>

        <div class="form-group">
        <input type="hidden" name="sql_query_id" value="{{page.sql_query.id}}" />
          <label for="sql_query" class="col-lg-2 control-label">SQL Query</label>
          <div class="col-lg-10">
            <textarea class="form-control" id="sql_query" name="sql_query_sql"  
                      rows="6" >{{page.sql_query.sql}}</textarea>
          </div>
        </div>
         <div class="form-group">
           <div class="col-lg-offset-2 col-lg-10">
          <button type="submit" class="btn btn-primary">Save and run</button>
        </div>
       </div>
      </form>
    
     %if page.report.name != '': 
        %include("datatables.tpl", datatable=page.datatable)
     %end
    
    %end
 </div>