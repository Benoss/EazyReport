<div class="col-lg-2">
   <ul class="nav  nav-pills nav-stacked">       
   %for group_name in page.chart_groups:    
       <li class="">
         <a href="?group={{ group_name }}">
         {{ group_name }}</a>
       </li>
    %end
   </ul>
</div>
   


<div class="col-lg-10" role="main">
 %for index, chart in enumerate(page.charts):
    <div class="col-lg-6">
        %include(chart.template, chart=chart)
    </div>
    %end
</div>
