<div class="col-md-2">
   <ul class="nav  nav-pills nav-stacked">       
   %for chart in page.charts:
       <li class='{{page.active(chart.name)}}'>
         <a href="?chart_id={{ chart.id }}&action=edit">{{ chart.name }}</a>
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
          <label for="chart_name" class="col-lg-2 control-label">Chart Name</label>
          <div class="col-lg-10">
            <input type="text" class="form-control" id="chart_name" name="name"  
                                 placeholder="chart Name" value="{{page.chart.name}}" />
          </div>
        </div>
        <div class="form-group">
          <label for="chart_description" class="col-lg-2 control-label">Chart Description</label>
          <div class="col-lg-10">
            <textarea class="form-control" id="chart_description" name="description"  
                      rows="3" >{{page.chart.description}}</textarea>
          </div>
        </div>
        <div class="form-group">
          <label for="chart_last_run" class="col-lg-2 control-label">Last Run</label>
          <div class="col-lg-2">
            <input type="text" disabled class="form-control" id="chart_last_run" name="last_run"  
                                 placeholder="Last Run" value="{{page.chart.last_run}}" />
          </div>
          <label for="chart_cache_duration" class="col-lg-2 control-label">Cache Duration</label>
          <div class="col-lg-2">
            <input type="text" class="form-control" id="chart_cache_duration" name=cache_duration  
                                 placeholder="Cache Duration" value="{{page.chart.cache_duration}}" />
          </div>
        </div>
        <div class="form-group">
          <label for="chart_group" class="col-lg-2 control-label">Group</label>
          <div class="col-lg-10">
            <input type="text" class="form-control" id="chart_group" name="group"  
                                 placeholder="Chart Group" value="{{page.chart.group}}" />
          </div>
        </div>

        <div class="form-group">
          <label for="sql_query" class="col-lg-2 control-label">SQL Query</label>
          <div class="col-lg-10">
            <textarea class="form-control" id="sql_query" name="sql"  
                      rows="6" >{{page.chart.sql}}</textarea>
          </div>
        </div>
         <div class="form-group">
           <div class="col-lg-offset-2 col-lg-10">
          <button type="submit" class="btn btn-primary">Save and run</button>
        </div>
       </div>
      </form>
    
     %if page.chart.name != '': 
        %include(page.highchart.template, chart=page.highchart)
     %end
    
    %end
 </div>