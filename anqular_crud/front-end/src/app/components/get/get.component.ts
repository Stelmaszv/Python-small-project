import { Component, OnInit  } from '@angular/core';
import { ListService } from '../../service/list.service'
import {ActivatedRoute} from '@angular/router';
import { List_Model } from  '../../model/list'
@Component({
  selector: 'app-get',
  templateUrl: './get.component.html',
  styleUrls: ['./get.component.sass']
})
export class GetComponent implements OnInit{
  item
  constructor(private listService:ListService,private route: ActivatedRoute) { }
  ngOnInit(): void {
    this.get_Data(this.route.snapshot.params.id)
  }
  get_Data(id){
    this.listService.get(id).subscribe(el => {
      this.item = el[];
    });
  }

}
