import { Component, OnInit} from '@angular/core';
import {FormControl, FormGroup} from '@angular/forms';
import { ListService } from '../../service/list.service'
import { Router } from '@angular/router';
import {ActivatedRoute} from '@angular/router';
@Component({
  selector: 'app-update',
  templateUrl: './update.component.html',
  styleUrls: ['./update.component.sass']
})
export class UpdateComponent implements OnInit {
  item: any
  id:number
  update:FormGroup
  constructor(private listService:ListService,private router: Router,private route: ActivatedRoute) {  }
  ngOnInit(): void {
    this.id=this.route.snapshot.params.id
    this.generate_form([])
    this.get(this.route.snapshot.params.id)
  }
  private get(id:number) : void{
    this.listService.get(id).subscribe(el => {
      this.generate_form(el)
    });
  }
  private generate_form(data:any) : void{
    this.update = new FormGroup({
      name: new FormControl(data.name),
    });
  }
  onSubmit() : void {
    this.listService.update(this.update.value,this.id).subscribe(el => {
      this.router.navigate(['/']);
    });
  }

}
