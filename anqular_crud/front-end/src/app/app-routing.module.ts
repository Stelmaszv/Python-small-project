import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { BaseComponent } from './components/base/base.component';
import { ListComponent } from './components/list/list.component'
import { CreateComponent } from './components/create/create.component';
import { GetComponent } from './components/get/get.component';
const routes: Routes = [
  { path:'' , component:ListComponent},
  { path:'create' , component: CreateComponent},
  { path:'item/:id' , component: GetComponent},
];

@NgModule({
  imports: [
    CommonModule,
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponents=[BaseComponent,ListComponent,CreateComponent,GetComponent]
