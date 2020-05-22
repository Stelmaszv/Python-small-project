import { Component, OnInit } from '@angular/core';
import { ListService } from '../../service/list.service'
import {ActivatedRoute} from '@angular/router';
import { Router } from '@angular/router';
@Component({
  selector: 'app-delete',
  templateUrl: './delete.component.html',
  styleUrls: ['./delete.component.sass']
})
export class DeleteComponent implements OnInit {

  constructor(private listService:ListService,private route: ActivatedRoute,private router: Router) { }

  ngOnInit(): void {
    this.delete(this.route.snapshot.params.id)
  }
  private delete(id) : void{
    this.listService.delete(id).subscribe(el => {
      this.router.navigate(['/']);
    });
  }
}
