import { Component, OnInit } from '@angular/core';
import { List_Model } from  '../../model/list'
@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.sass']
})
export class ListComponent implements OnInit {
  list:List_Model[];
  constructor() { }

  ngOnInit(): void {
  }

}
