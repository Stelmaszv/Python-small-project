import { Component, OnInit } from '@angular/core';
import { ListService } from '../../service/list.service'
import { List_Model } from  '../../model/list'
@Component({
  selector: 'app-base',
  templateUrl: './base.component.html',
  styleUrls: ['./base.component.sass']
})
export class BaseComponent implements OnInit {
  list:List_Model[];
  constructor(private listService:ListService) { }

  ngOnInit(): void {
    this.listService.getList().subscribe(items => {
      console.log(items)
      this.list=items
    });
  }
}
