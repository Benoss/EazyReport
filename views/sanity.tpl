<div class="col-lg-2">
   <ul class="nav  nav-stacked">       
   %for model in page.model_list:    
       <li class="{{page.active(model.name)}} ">
         <a href="?sanity={{ model.name }}" class='label label-{{ page.get_danger(model.id) }}'>
         <span class="badge pull-right">{{ model.nb_rows }}</span>
         {{ model.name }}</a>
       </li>
    %end
   </ul>
</div>
   
 <div class="col-lg-10" role="main">
%if page.current_report:
<div class="col-lg-12">
	<p>{{ model.name }}</p>
    <p>{{ page.current_report.description }}</p>
    <p>Last report was run {{ page.current_report.last_run.strftime('%c') }}</p>
</div>

<div class="col-lg-12">
    %include("datatables.tpl", datatable=page.datatable)
 </div>
 %end