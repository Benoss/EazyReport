<div class="col-lg-2">
   <ul class="nav  nav-pills nav-stacked">       
   %for model in page.model_list:    
       <li class="{{page.active(model.name)}}">
         <a href="?report={{ model.name }}">
         <span class="badge pull-right">{{ model.nb_rows }}</span>
         {{ model.name }}</a>
       </li>
    %end
   </ul>
</div>
   
 <div class="col-lg-10" role="main">
%if page.current_report:
<div class="col-lg-12">
    <p>{{ page.current_report.description }}</p>
    <p>Last report was run {{ page.current_report.last_run.strftime('%c') }}</p>
</div>

<div class="col-lg-12">
    %include("datatables.tpl", datatable=page.datatable)
 </div>
 %end