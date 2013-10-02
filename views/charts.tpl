<div class="col-lg-2">
   <ul class="nav  nav-pills nav-stacked">       

   </ul>
</div>
   


<div class="col-lg-10" role="main">
 %for index, chart in enumerate(page.charts):
    <div class="col-lg-6">
        %include(chart.template, chart=chart)
    </div>
    %end
</div>
