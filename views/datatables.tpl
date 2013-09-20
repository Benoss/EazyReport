<div class="scrollable">
     <table class="table table-striped table-condensed" id="{{ datatable.id_table }}">
       <thead>
         <tr>
             %for col_header in datatable.header:
             <th>{{ col_header }}</th>
             %end
         </tr>
        </thead>
        <tbody>
        </tbody>
        <tfoot>
          <tr>
             %for col_header in datatable.header:
             <th id="foot_{{ datatable.id_table }}"><input type="text" name="{{datatable.slugify(col_header)}}" placeholder="{{col_header}}" value="" class="search_init form-control input-small" /></th>
             %end
         </tr>
        <tfoot>
     </table>
     </div>