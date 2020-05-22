import { Component, OnInit } from '@angular/core';
import { List_Model } from  '../../model/list'
import { ListService } from '../../service/list.service'
@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.sass']
})
export class ListComponent implements OnInit {
  list:List_Model[];
  constructor(private listService:ListService) { }

  ngOnInit(): void {
    this.getlist()
  }
  private getlist () :any {
    this.listService.getList().subscribe(items => {
      this.list=items
    });
  }

}
